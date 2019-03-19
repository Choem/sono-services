import { CallHandler, ExecutionContext, NestInterceptor } from '@nestjs/common';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { APIResponse } from '../baseController';
import { classToPlain } from 'class-transformer';

export class TransformInterceptor implements NestInterceptor<any, any> {
  intercept(
    context: ExecutionContext,
    next: CallHandler<APIResponse | any>,
  ): Observable<APIResponse | any> {
    return next.handle().pipe(
      map(data => {
        return classToPlain(data);
      }),
    );
  }
}
