from django.contrib import admin
from multimedia.models import Multimedia, MultimediaComment


class CommentInline(admin.TabularInline):
    model = MultimediaComment
    max_num = 5
    extra = 1
    readonly_fields = (
        'created',
    )

    fieldsets = (
        ('Comments', {
            'classes': ('collapse',),
            'fields': (
                ('author', 'created'),
                'heading',
                'body',
            )                
        }),
    )

class MultimediaAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    readonly_fields = (
        'uploaded_on',
        'last_edited',
    )
    fieldsets = (
        (None, {'fields': ( 
                    ('category', 'subcategory', 'level'),
                    ('title', 'resource', 'caption_overlay'),
                    'description',
                    ('uploaded_by', 'uploaded_on', 'last_edited'),
                    ('organization', 'owner', 'owner_url'),
                    'tags',
                    )
                }
        ),
    )
    list_display = ('category', 'subcategory', 'title',)

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', 'js/libs/tiny_mce/tinymce_setup.js',)
        
admin.site.register(Multimedia, MultimediaAdmin)