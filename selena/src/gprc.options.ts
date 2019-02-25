import { Transport, ClientOptions } from '@nestjs/microservices';
import { join } from 'path';
import { Config } from './utils/Config';

const protoPath = join(__dirname, '..', '..', 'shared', 'protos', 'selena_service', 'selena_service.proto');
const loaderDir = join(__dirname, '..', '..', 'shared', 'protos', '**/*.proto');

export const grpcClientOptions: ClientOptions = {
  transport: Transport.GRPC,
  options: {
    url: `${Config.getString('APP_HOST')}:${Config.getString('GRPC_PORT')}`,
    package: 'sono',
    protoPath,
    loader: {
      includeDirs: [loaderDir],
    },
  },
};
