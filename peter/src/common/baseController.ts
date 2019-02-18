import { classToPlain, Exclude } from 'class-transformer';

export interface IAPIResponse {
  label?: string;
  error?: any;
  data?: any;
  args?: any[];
}

export class APIResponse {
  @Exclude()
  public label?: string;

  public message?: string;
  public error?: any;
  public data?: any;

  @Exclude()
  public args?: any[];

  constructor(public success: boolean, options: IAPIResponse) {
    this.label = options.label;
    this.error = options.error;
    this.data = options.data;
    this.args = options.args;
  }
}

export abstract class BaseController {
  public api(success: boolean, options?: IAPIResponse): APIResponse {
    return new APIResponse(success, options);
  }
}
