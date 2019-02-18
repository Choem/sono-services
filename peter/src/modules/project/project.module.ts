import { Module } from '@nestjs/common';
import { ProjectEntity } from '../../entities/project.entity';
import { ProjectController } from './controllers/project/project.controller';
import { ProjectService } from './services/project/project.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { APP_INTERCEPTOR } from '@nestjs/core';
import { TranslateInterceptor } from '../../common/interceptors/translate.interceptor';
import * as path from 'path';

@Module({
  imports: [TypeOrmModule.forFeature([ProjectEntity])],
  controllers: [ProjectController],
  providers: [
    ProjectService,
    {
      provide: APP_INTERCEPTOR,
      useValue: new TranslateInterceptor(
        path.join(__dirname, '/i18n/'),
        ProjectModule,
      ),
    },
  ],
  exports: [ProjectService],
})
export class ProjectModule {}
