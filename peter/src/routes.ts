import { Routes } from 'nest-router';
import { ProjectModule } from './modules/project/project.module';
export const routes: Routes = [
  {
    path: '/projects',
    module: ProjectModule,
  }
];
