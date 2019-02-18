import {
  Column,
  Entity, JoinColumn, ManyToOne, PrimaryColumn,
} from 'typeorm';
import { ProjectEntity } from './project.entity';

@Entity('project_member')
export class ProjectMemberEntity {
  @PrimaryColumn({name: 'user_id'})
  userId: number;

  @ManyToOne(type => ProjectEntity, project => project.members)
  @JoinColumn({name: 'project_id'})
  project: ProjectEntity;

  @PrimaryColumn({name: 'project_id'})
  projectId: number;
}
