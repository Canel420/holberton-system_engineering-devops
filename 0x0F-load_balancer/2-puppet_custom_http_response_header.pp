# Install HTTP header on ubuntu server.
exec { 'HTTP_header_Puppet':
  command  => 'sudo apt -y update;
               sudo apt -y install nginx;
               service nginx start;
               sudo chmod 777 /etc/nginx;
               sudo chmod 777 /etc/nginx/nginx.conf;
               sudo sed -i "/sendfile on;/ a \\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf;
               sudo service nginx restart',
  provider => 'shell',
}
