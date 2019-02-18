import { INestApplication } from '@nestjs/common';
import * as request from 'supertest';
import { createApp } from '../src/app';
import { Config } from '../src/utils/config';
import * as dotenv from 'dotenv';

dotenv.config({path: '.env.test'});

describe('AppController (e2e)', () => {
  let app: INestApplication;
  let server;

  beforeAll(async (done) => {
    app = await createApp();

    await app.listen(Config.getInt('APP_PORT'), () => {
      server = app.getHttpServer().getInstance().server;
      done();
    });
  });

  afterAll(async (done) => {
    app.close().then(() => {
      done();
    }).catch(error => {
      console.log(error);
      throw error;
    });
  });

  it('/ (GET)', () => {
    return request(server)
      .get('/')
      .expect(404);
  });

  it('/docs (GET)', () => {
    return request(server)
      .get('/docs/index.html')
      .expect(200);
  });
});
