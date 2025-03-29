# Generated by Django 4.1 on 2025-03-29 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chatterbot', '0019_alter_statement_id_alter_tag_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='conversation',
            field=models.CharField(help_text='A label used to link this statement to a conversation.', max_length=32),
        ),
        migrations.AlterField(
            model_name='statement',
            name='in_response_to',
            field=models.CharField(help_text='The text of the statement that this statement is in response to.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='persona',
            field=models.CharField(help_text='A label used to link this statement to a persona.', max_length=50),
        ),
        migrations.AlterField(
            model_name='statement',
            name='search_in_response_to',
            field=models.CharField(blank=True, help_text='A modified version of the in_response_to text optimized for searching.', max_length=255),
        ),
        migrations.AlterField(
            model_name='statement',
            name='search_text',
            field=models.CharField(blank=True, help_text='A modified version of the statement text optimized for searching.', max_length=255),
        ),
        migrations.AlterField(
            model_name='statement',
            name='tags',
            field=models.ManyToManyField(help_text='The tags that are associated with this statement.', related_name='statements', to='django_chatterbot.tag'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='text',
            field=models.CharField(help_text='The text of the statement.', max_length=255),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.SlugField(help_text='The unique name of the tag.', unique=True),
        ),
    ]
