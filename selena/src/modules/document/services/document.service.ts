import { Injectable, Logger, OnModuleInit } from '@nestjs/common';
import * as ShareDB from 'sharedb';
import * as shareMongo from 'sharedb-mongo';

@Injectable()
export class DocumentService implements OnModuleInit {
  private db;
  private backend;

  constructor(private logger: Logger) { }

  onModuleInit(): any {
    this.db = shareMongo('mongodb://192.168.99.101:27017/test');
    this.backend = new ShareDB({ db: this.db });
    this.createDoc();
  }

  createDoc() {
    const connection = this.backend.connect();
    const doc = connection.get('selena', 'project');
    doc.fetch(res => {
      if (doc.type == null) {
        doc.create({projectFile: 'test'});
        return;
      }
    });
  }

  getBackend() {
    return this.backend;
  }
}
