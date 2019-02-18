import { FastifyAdapter, NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';

import { INestApplication, INestFastifyApplication } from '@nestjs/common';
import { grpcClientOptions } from './grpc.options';


export async function createApp(): Promise<
  INestApplication & INestFastifyApplication
> {
  const fastifyAdapter = new FastifyAdapter({ trustProxy: true });
  const app = await NestFactory.create(AppModule, fastifyAdapter, {
    cors: true,
  });

  app.connectMicroservice(grpcClientOptions);
  app.register(require('fastify-multipart'));
  app.register(require('fastify-helmet'));

  const options = new DocumentBuilder()
    .setTitle('Sono Project API')
    .setDescription('description...')
    .setVersion('1.0')
    .build();

  const document = SwaggerModule.createDocument(app, options);
  SwaggerModule.setup('docs', app, document);

  return app;
}
