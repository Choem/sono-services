import { Logger, Module } from '@nestjs/common';
import { DocumentGateway } from './gateways/document.gateway';
import { DocumentService } from './services/document.service';

@Module({
  providers: [
    DocumentGateway,
    DocumentService,
    { provide: Logger, useValue: new Logger('document') },
  ],
  exports: [DocumentService],
})
export class DocumentModule {}
