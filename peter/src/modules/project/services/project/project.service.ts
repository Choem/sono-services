import { HttpStatus, Injectable } from '@nestjs/common';
import { ProjectCreateDto } from '../../dtos/projectCreateDto';
import { ApiException } from '../../../../common/exceptions/apiException';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { ProjectEntity } from '../../../../entities/project.entity';

@Injectable()
export class ProjectService {
  constructor(
    @InjectRepository(ProjectEntity)
    private readonly projectRepository: Repository<ProjectEntity>,
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
    return this.projectRepository.insert(project);
  }

  async getAll(
    pageSize: number = 10,
    page: number = 0
  ){
    return this.projectRepository
      .createQueryBuilder('project')
      .skip(page * pageSize)
      .take(pageSize)
      .getManyAndCount();
  }
}
