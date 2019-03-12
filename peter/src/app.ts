import { FastifyAdapter, NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';

import { INestApplication, INestFastifyApplication } from '@nestjs/common';
import { grpcClientOptions } from './grpc.options';
import { Config } from './utils/config';


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
    .setSchemes('https', 'http')
    .setVersion('1.0')
    .setBasePath(Config.getString('SWAGGER_BASE_PATH'))
    .build();

  const document = SwaggerModule.createDocument(app, options);
  SwaggerModule.setup('docs', app, document);

  return app;
}
