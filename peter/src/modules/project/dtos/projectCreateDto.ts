import { ProjectEntity } from '../../../entities/project.entity';
import { ApiModelProperty, ApiModelPropertyOptional } from '@nestjs/swagger';
import {
  IsString,
} from 'class-validator';

export class ProjectCreateDto {
  @IsString()
  @ApiModelProperty()
  readonly name: string;

  toProject(): ProjectEntity {
    const project = new ProjectEntity();
    project.name = this.name;
    return project;
  }
}
