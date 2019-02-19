import { FastifyAdapter, NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { WsAdapter } from '@nestjs/websockets';
import * as dotenv from 'dotenv';
import { Config } from './utils/Config';

dotenv.config();

// needs to be imported after dotenv config
import { createApp } from './app';

async function bootstrap() {
  const app = await createApp();
  await app.listen(Config.getInt('APP_PORT'), Config.getString('APP_HOST'));
  await app.startAllMicroservicesAsync();

  process.on('SIGTERM', async () => {
    await shutdown(app);
  });

  process.on('SIGINT', async  () => {
    await shutdown(app);
  });

}

async function shutdown(app: any) {
  app.close().then(() => {
    process.exit(0);
  }).catch(error => {
    process.exit(1);
  });
}

bootstrap().then(() => {
  if (process.send) { process.send('ready'); }
});
