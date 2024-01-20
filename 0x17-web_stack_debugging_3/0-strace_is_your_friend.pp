# debugging apache 500 error
exec { 'replaces wrong php filetype':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
