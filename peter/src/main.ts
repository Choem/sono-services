import 'reflect-metadata';
import { Config } from './utils/config';
import * as dotenv from 'dotenv';
import * as path from 'path';
import * as fs from 'fs';

dotenv.config();

if(Config.getString('ENVIRONMENT') === 'development'){
  const devenv = dotenv.parse(fs.readFileSync(path.join(__dirname, '../../shared/.env.development')));
  for (let k in devenv) {
    process.env[k] = devenv[k];
  }
}

// needs to be imported after dotenv config
import { createApp } from './app';

async function bootstrap() {
  const app = await createApp();

  await app.listen(Config.getInt('APP_PORT'), Config.getString('APP_HOST'));
  await app.startAllMicroservicesAsync();

  process.on('SIGTERM', async () => {
    await shutdownApp(app);
  });

  process.on('SIGINT', async () => {
    await shutdownApp(app);
  });
}

async function shutdownApp(app: any) {
  app
    .close()
    .then(() => {
      process.exit(0);
    })
    .catch(error => {
      process.exit(1);
    });
}

bootstrap()
  .then(() => {
    if (process.send) {
      process.send('ready');
    }
  })
  .catch(console.log);
