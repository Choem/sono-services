import { Test, TestingModule } from '@nestjs/testing';
import { SelenaService } from './selena.service';

describe('SelenaService', () => {
  let service: SelenaService;

  beforeAll(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [SelenaService],
    }).compile();
    service = module.get<SelenaService>(SelenaService);
  });
  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
