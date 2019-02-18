import { Logger, Module } from '@nestjs/common';
import { DocumentModule } from './modules/document/document.module';

@Module({
  imports: [DocumentModule],
  controllers: [],
  providers: [
    { provide: Logger, useValue: new Logger('APP') },
  ],
})
export class AppModule {}
