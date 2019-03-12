import { Controller } from '@nestjs/common';
import { GrpcMethod } from '@nestjs/microservices';
import { DocumentService } from '../services/document.service';

@Controller()
export class DocumentController {
  constructor(private readonly documentService: DocumentService) {
  }

  @GrpcMethod('DocumentService')
  async createDoc(data: { id: number, songdata: string }) {
    await this.documentService.createDoc(data.id, data.songdata);
    return { success: true };
  }
}
