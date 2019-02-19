import { Logger, Module } from '@nestjs/common';
import { DocumentGateway } from './gateways/document.gateway';
import { DocumentService } from './services/document.service';
import { DocumentController } from './controllers/document.controller';

@Module({
  controllers: [
    DocumentController,
  ],
  providers: [
    DocumentGateway,
    DocumentService,
    { provide: Logger, useValue: new Logger('document') },
  ],
  exports: [DocumentService],
})
export class DocumentModule {}
