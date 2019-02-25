import { Transport, ClientOptions } from '@nestjs/microservices';
import { Config } from './utils/config';

const protoPath = Config.getProtoPath('peter_service', 'peter_service.proto');
const loaderDir = Config.getProtoPath('protos', '**/*.proto');

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
