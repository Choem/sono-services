import { ExecutionContext, NestInterceptor } from '@nestjs/common';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { classToPlain } from 'class-transformer';
import { APIResponse } from '../baseController';
import * as fs from 'fs';
import * as path from 'path';
import { format as stringFormat } from 'util';
import { MODULE_PATH } from '@nestjs/common/constants';

export class TranslateInterceptor implements NestInterceptor<any, any> {
  module: any;

  translations: {
    [key: string]: object;
  } = {};

  constructor(i18nPath: string, module: any = null) {
    this.module = module;

    if (!fs.existsSync(i18nPath)) {
      throw Error('i18n path does not exists');
    }

    fs.readdir(i18nPath, (err, files) => {
      files
        .filter(file => {
          return file.endsWith('.json');
        })
        .forEach(file => {
          const data = fs.readFileSync(path.join(i18nPath, file), 'utf8');
          this.translations[file.replace('.json', '')] = JSON.parse(data);
        });
    });
  }

  intercept(
    context: ExecutionContext,
    call$: Observable<APIResponse | any>,
  ): Observable<APIResponse | any> {
    const url = context.switchToHttp().getRequest().raw.url;
    if (url.startsWith(Reflect.getMetadata(MODULE_PATH, this.module))) {
      return call$.pipe(
        map(data => {
          if (
            data instanceof APIResponse &&
            data.label !== undefined &&
            data.label.length > 0
          ) {
            try {
              data.message = stringFormat(
                this.translations.en[data.label],
                ...(data.args || []),
              );
            } catch (e) {
              data.message = `No message found for: ${data.label}`;
            }
          }

          return classToPlain(data);
        }),
      );
    }

    return call$;
  }
}
