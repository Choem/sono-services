import { FastifyAdapter, NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { WsAdapter } from '@nestjs/websockets';
import * as dotenv from 'dotenv';
import { Config } from './utils/Config';
import { grpcClientOptions } from './gprc.options';

dotenv.config();

async function bootstrap() {
  const fastifyAdapter = new FastifyAdapter({trustProxy: true});
  const app = await NestFactory.create(AppModule, fastifyAdapter, {cors: true});
  // app.useWebSocketAdapter(new WsAdapter(app));

  // app.connectMicroservice(grpcClientOptions);

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
