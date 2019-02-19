import { Transport, ClientOptions } from '@nestjs/microservices';
import { join } from 'path';
import { Config } from './utils/config';

let protoPath = join(__dirname, '..', '..', 'shared', 'protos', 'peter.proto');
let loaderDir = join(__dirname, '..', '..', 'shared', 'protos', '**/*.proto');

if(Config.getString('ENVIRONMENT') !== 'development') {
  protoPath = join(__dirname, '..', 'shared', 'protos', 'peter.proto');
  loaderDir = join(__dirname, '..', 'shared', 'protos', '**/*.proto');
}

export const grpcClientOptions: ClientOptions = {
  transport: Transport.GRPC,
  options: {
    url: `${Config.getString('APP_HOST')}:${Config.getString('GRPC_PORT')}`,
    package: 'sono',
    protoPath: protoPath,
    loader: {
      includeDirs: [loaderDir],
    }
  },
};
