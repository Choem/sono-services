import { Injectable, Logger, OnModuleInit } from '@nestjs/common';
import * as ShareDB from 'sharedb';
import * as shareMongo from 'sharedb-mongo';
import { Config } from '../../../utils/config';

@Injectable()
export class DocumentService implements OnModuleInit {
  private db;
  private backend;
  private connection;

  constructor(private logger: Logger) { }

  onModuleInit(): any {
    this.db = shareMongo(Config.getString('MONGO_DB'));
    this.backend = new ShareDB({ db: this.db });
    this.connection = this.backend.connect();
  }

  createDoc(projectId: number) {
    const doc = this.connection.get('selena', projectId.toString());
    doc.fetch(() => {
      if (doc.type == null) {
        doc.create({data: null});
      }
    });
  }

  getBackend() {
    return this.backend;
  }
}
