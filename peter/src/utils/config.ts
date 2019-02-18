import * as path from 'path';

export class Config {
  public static getBool(name: string): boolean {
    return this.getString(name) === 'true';
  }

  public static getString(name: string): string {
    return process.env[name];
  }

  public static getInt(name: string): number {
    return parseInt(this.getString(name), 10);
  }

  public static get isProduction(): boolean {
    return this.getBool('PRODUCTION');
  }

  public static get appRoot(): string {
    return (global as any).appRoot;
  }

  public static getViewPath(currentDir: string, viewPath: string) {
    return path.relative(Config.appRoot, path.join(currentDir, viewPath));
  }
}
