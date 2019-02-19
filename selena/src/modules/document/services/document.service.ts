import { Injectable, Logger, OnModuleInit } from '@nestjs/common';
import * as ShareDB from 'sharedb';
import * as shareMongo from 'sharedb-mongo';

@Injectable()
export class DocumentService implements OnModuleInit {
  private db;
  private backend;
  private connection;

  constructor(private logger: Logger) { }

  onModuleInit(): any {
    this.db = shareMongo('mongodb://192.168.99.101:27017/selena');
    this.backend = new ShareDB({ db: this.db });
    this.connection = this.backend.connect();
  }

  createDoc(projectId: number) {
    const doc = this.connection.get('selena', projectId.toString());
    doc.fetch(res => {
      if (doc.type == null) {
        doc.create({});
      }
    });
  }

  getBackend() {
    return this.backend;
  }
}
