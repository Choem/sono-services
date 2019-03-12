import { Injectable } from '@nestjs/common';
import * as protoLoader from '@grpc/proto-loader';
import { Config } from '../../../../utils/config';
import * as grpc from 'grpc';

@Injectable()
export class SelenaService {
  client;

  constructor() {
    const proto = grpc.loadPackageDefinition(
      protoLoader.loadSync( Config.getProtoPath('selena_service/selena_service.proto'), {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
      }),
    );

    const GRPC_HOST = `${Config.getString('SELENA_HOST')}:${Config.getString('SELENA_PORT')}`;
    this.client = new proto.sono.DocumentService(GRPC_HOST, grpc.credentials.createInsecure());
  }

  createDoc(projectId: number) {
    return new Promise((resolve, reject) => {
      this.client.CreateDoc({id: projectId}, (err, res) => {
        if (err) {
          reject(err);
        }
        resolve(res);
      });
    });
  }

}
