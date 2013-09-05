require 'find'

http_path = '/'
css_dir = (environment == :development) ? 'project/static/styles-dev' : 'project/static/styles'
sass_dir = 'project/sass'
images_dir = 'project/static/images'
javascripts_dir = 'project/static/scripts'
http_generated_images_path = '../images'

output_style = (environment == :development) ? :expanded : :compact
line_comments = (environment == :development) ? true : false

relative_assets = true

preferred_syntax = :sass

python_path = `python -c "import sys; sys.stdout.write(':'.join(sys.path))"`
python_path = python_path.split(':').find_all {|path| FileTest.exists? path}

Find.find(*python_path) do |filepath|
  name = File.basename(filepath)
  if name.index('.')
    Find.prune
  elsif FileTest.directory? filepath and ( name == 'sass')
    add_import_path filepath
  end
end
