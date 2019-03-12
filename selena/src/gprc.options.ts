import { Transport, ClientOptions } from '@nestjs/microservices';
import { Config } from './utils/config';

const protoPath = Config.getProtoPath('selena_service/selena_service.proto');
const loaderDir =  Config.getProtoPath('**/*.proto');

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

// docker run -e APP_PORT=3333 -e GRPC_PORT=50051 -e APP_HOST='0.0.0.0' -e DB_DRIVER='mysql' -e DB_HOST='localhost' -e DB_PORT=3306 -e DB_USERNAME='root' -e DB_PASSWORD='root' -e DB_NAME='sono_peter' -e SELENA_HOST='127.0.0.1' -e SELENA_PORT=50052 --network=host sono-studio/peter:v6
