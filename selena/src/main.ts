import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { WsAdapter } from '@nestjs/websockets';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useWebSocketAdapter(new WsAdapter(app.getHttpServer()));
  await app.listen(3000);

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
