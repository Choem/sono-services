import {
  Column,
  Entity, OneToMany,
  PrimaryGeneratedColumn,
} from 'typeorm';
import { ProjectMemberEntity } from './project_member.entity';

@Entity('project')
export class ProjectEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({name: 'document_id', nullable: true})
  documentId: string;

  @Column({name: 'user_id'})
  userId: number;

  @Column({name: 'name'})
  name: string;

  @OneToMany(type => ProjectMemberEntity, member => member.project)
  members: ProjectMemberEntity[];

}
