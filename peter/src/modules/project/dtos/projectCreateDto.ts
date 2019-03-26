import { ProjectEntity } from '../../../entities/project.entity';
import { ApiModelProperty, ApiModelPropertyOptional } from '@nestjs/swagger';
import {
  IsOptional,
  IsString,
} from 'class-validator';

export class ProjectCreateDto {
  @IsString()
  @ApiModelProperty()
  readonly name: string;

  @IsString()
  @IsOptional()
  @ApiModelPropertyOptional()
  readonly description?: string;

  toProject(): ProjectEntity {
    const project = new ProjectEntity();
    project.name = this.name;
    project.description = this.description;
    return project;
  }
}
