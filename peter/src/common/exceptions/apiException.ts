import { HttpStatus } from '@nestjs/common';

export class ApiException {
  constructor(
    public status: HttpStatus,
    public label: string,
    public args: any[] = [],
    public message?: string,
  ) {}
}
