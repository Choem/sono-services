import { HttpStatus, Injectable } from '@nestjs/common';
import { ProjectCreateDto } from '../../dtos/projectCreateDto';
import { ApiException } from '../../../../common/exceptions/apiException';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { ProjectEntity } from '../../../../entities/project.entity';
import { SelenaService } from '../selena/selena.service';

@Injectable()
export class ProjectService {
  constructor(
    @InjectRepository(ProjectEntity)
    private readonly projectRepository: Repository<ProjectEntity>,
    private readonly selenaService: SelenaService,
  ) {}

  async create(projectCreateDto: ProjectCreateDto) {
    const foundProject = await this.projectRepository
      .createQueryBuilder('project')
      .where('project.name = :name', {name: projectCreateDto.name})
      .getOne();

    if (foundProject !== undefined) {
      throw new ApiException(
        HttpStatus.BAD_REQUEST,
        'project.alreadyExists',
        [foundProject.name],
      );
    }

    const project = projectCreateDto.toProject();
    project.userId = 0;
    const result = await this.projectRepository.insert(project);
    try {
      await this.selenaService.createDoc(project.id);
    } catch (e) {
      // no implementation needed
    }
    return result;
  }

  async findById(id: number) {
    return this.projectRepository.findOne(id);
  }

  async getAll(
    pageSize: number = 10,
    page: number = 0,
  ) {
    return this.projectRepository
      .createQueryBuilder('project')
      .skip(page * pageSize)
      .take(pageSize)
      .getManyAndCount();
  }
}
