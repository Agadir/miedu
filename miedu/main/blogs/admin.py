from django.contrib import admin
from blogs.models import Post, BlogComment

class CommentInline(admin.TabularInline):
    model = BlogComment
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

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    search_fields = ["title"]
    readonly_fields = ("created",)
    fieldsets = (
        (None, {'fields': ( 
        			('title', 'author', 'created'),
                    ('category', 'subcategory'),
                    ('photo', 'link'),
                    'tagline',
                    'body',
                    'tags',
                    )
                }
        ),
    )

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', 'js/libs/tiny_mce/tinymce_setup.js',)

admin.site.register(Post, PostAdmin)