import {
  OnGatewayConnection,
  SubscribeMessage,
  WebSocketGateway,
  WebSocketServer, WsAdapter,
} from '@nestjs/websockets';
import { DocumentService } from '../services/document.service';
import * as WebSocketJsonStream from 'websocket-json-stream';

@WebSocketGateway()
export class DocumentGateway implements OnGatewayConnection {
  constructor(private readonly documentService: DocumentService) {}

  @WebSocketServer() server;

  handleConnection(client: any, ...args: any[]): any {
    const stream = new WebSocketJsonStream(client);
    this.documentService.getBackend().listen(stream);
  }
}
