import { Logger, Module, OnModuleInit, ValidationPipe } from '@nestjs/common';
import { TypeOrmModule, TypeOrmModuleOptions } from '@nestjs/typeorm';
import { RouterModule } from 'nest-router';
import { routes } from './routes';
import { Connection } from 'typeorm';
import { ProjectModule } from './modules/project/project.module';
import { APP_FILTER, APP_PIPE } from '@nestjs/core';
import { Config } from './utils/config';
import * as path from 'path';
import { ApiExceptionFilter } from './common/filters/api-exception.filter';

@Module({
  imports: [
    RouterModule.forRoutes(routes),
    TypeOrmModule.forRoot({
      type: Config.getString('DB_DRIVER'),
      host: Config.getString('DB_HOST'),
      port: Config.getInt('DB_PORT'),
      username: Config.getString('DB_USERNAME'),
      password: Config.getString('DB_PASSWORD'),
      database: Config.getString('DB_NAME'),
      logging: Config.getBool('DB_LOGGING'),
      entities: [path.join(__dirname, `entities/**/**.entity${path.extname(__filename)}`)],
      migrations: [path.join(__dirname, `migrations/**/**${path.extname(__filename)}`)],
      extra: {
        charset: Config.getString('DB_CHARSET'),
      },
    } as TypeOrmModuleOptions),
    ProjectModule,
  ],
  controllers: [],
  providers: [
    { provide: Logger, useValue: new Logger('APP') },
    { provide: APP_PIPE, useValue: new ValidationPipe({ transform: true }) },
    {
      provide: APP_FILTER,
      useClass: ApiExceptionFilter,
    },
  ],
})
export class AppModule implements OnModuleInit {
  constructor(
    private readonly connection: Connection,
    private readonly logger: Logger,
  ) {}


  async onModuleInit() {
    this.connection
      .runMigrations({ transaction: true })
      .then(() => {
        this.logger.log('migrations done');
      })
      .catch(err => {
        this.logger.error(`migrations failed ${err.message}`);
      });
  }
}
