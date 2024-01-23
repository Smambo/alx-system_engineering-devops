# Puppet script  changes OS configuration to make it possible
# to login with the `holberton` user and open files without errors.
exec {
  '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf':
}
