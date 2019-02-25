import { FastifyAdapter, NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { INestApplication, INestFastifyApplication } from '@nestjs/common';
import { grpcClientOptions } from './gprc.options';
import { WsAdapter } from '@nestjs/websockets';

export async function createApp(): Promise<
  INestApplication & INestFastifyApplication
  > {
  const fastifyAdapter = new FastifyAdapter({ trustProxy: true });
  const app = await NestFactory.create(AppModule, fastifyAdapter, {
    cors: true,
  });
  app.useWebSocketAdapter(new WsAdapter(app));

  app.connectMicroservice(grpcClientOptions);

  return app;
}
