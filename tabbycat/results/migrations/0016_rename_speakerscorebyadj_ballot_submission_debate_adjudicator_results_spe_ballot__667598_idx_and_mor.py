# Generated by Django 5.0.4 on 2024-05-04 13:21

import utils.models
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adjallocation', '0010_alter_adjudicatoradjudicatorconflict_unique_together_and_more'),
        ('draw', '0009_alter_teamsideallocation_unique_together_and_more'),
        ('motions', '0006_alter_debateteammotionpreference_unique_together_and_more'),
        ('participants', '0022_rename_team_tournament_institution_short_reference_participant_tournam_160efa_idx_and_more'),
        ('results', '0015_alter_ballotsubmission_submitter_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='speakerscorebyadj',
            new_name='results_spe_ballot__667598_idx',
            old_fields=('ballot_submission', 'debate_adjudicator'),
        ),
        migrations.RenameIndex(
            model_name='teamscorebyadj',
            new_name='results_tea_ballot__a296a6_idx',
            old_fields=('ballot_submission', 'debate_adjudicator'),
        ),
        migrations.AlterUniqueTogether(
            name='ballotsubmission',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='speakerscore',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='speakerscorebyadj',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='teamscore',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='teamscorebyadj',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='ballotsubmission',
            constraint=utils.models.UniqueConstraint(fields=('debate', 'version'), name='results_ballotsubmission_debate__version_uniq'),
        ),
        migrations.AddConstraint(
            model_name='speakerscore',
            constraint=utils.models.UniqueConstraint(fields=('debate_team', 'position', 'ballot_submission'), name='results_speakerscore_debate_team__position__ballot_submission_uniq'),
        ),
        migrations.AddConstraint(
            model_name='speakerscorebyadj',
            constraint=utils.models.UniqueConstraint(fields=('debate_adjudicator', 'debate_team', 'position', 'ballot_submission'), name='results_speakerscorebyadj_debate_adjudicator__debate_team__position__ballot_submission_uniq'),
        ),
        migrations.AddConstraint(
            model_name='teamscore',
            constraint=utils.models.UniqueConstraint(fields=('debate_team', 'ballot_submission'), name='results_teamscore_debate_team__ballot_submission_uniq'),
        ),
        migrations.AddConstraint(
            model_name='teamscorebyadj',
            constraint=utils.models.UniqueConstraint(fields=('debate_adjudicator', 'debate_team', 'ballot_submission'), name='results_teamscorebyadj_debate_adjudicator__debate_team__ballot_submission_uniq'),
        ),
    ]
