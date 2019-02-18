import 'reflect-metadata';
import { Config } from './utils/config';
import * as dotenv from 'dotenv';

dotenv.config();

// needs to be imported after dotenv config
import { createApp } from './app';

async function bootstrap() {
  const app = await createApp();

  console.log(process.env);

  await app.listen(Config.getInt('APP_PORT'));

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
