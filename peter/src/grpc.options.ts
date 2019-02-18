import { Transport, ClientOptions } from '@nestjs/microservices';
import { join } from 'path';

export const grpcClientOptions: ClientOptions = {
  transport: Transport.GRPC,
  options: {
    url: '127.0.0.1:50051',
    package: 'project',
    protoPath: join(__dirname, './project.proto'),
  },
};
