import { ExceptionFilter, Catch, ArgumentsHost } from '@nestjs/common';
import { HttpException } from '@nestjs/common';
import { ApiException } from '../exceptions/apiException';

@Catch(ApiException)
export class ApiExceptionFilter implements ExceptionFilter {
  catch(exception: ApiException | any, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const reply = ctx.getResponse();
    const request = ctx.getRequest();
    const status = exception instanceof  ApiException ? exception.status : 500;

    console.log(exception);

    reply.code(status).send({
      status: status,
      message: exception.label
    });
  }
}
