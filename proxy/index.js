var http = require('http'),
  httpProxy = require('http-proxy'),
  commandLineArgs = require('command-line-args'),
  commandLineUsage = require('command-line-usage');

const optionDefs = [
  { name: 'host', alias: 'h', type: String, defaultValue: 'pc09785' },
  { name: 'port', alias: 'p', type: String, defaultValue: 8070 },
  { name: 'named', alias: 'n', type: String }
];

const cli = commandLineArgs(optionDefs, { stopAtFirstUnknown: true });

const namedWorkstations = {
  'mitch': { host: 'lt12283', port: 8070 },
  'patrick': { host: 'lt10288', port: 8070 }
}

let target = 'http://' + cli.host + ':' + cli.port + '/';

if (cli.named) {
  let workstation = namedWorkstations[cli.named]
  if (workstation) {
    target = 'http://' + workstation.host + ':' + workstation.port + '/';
  }
}
if (cli._unknown) {
  console.log('Usage:')
  console.log('--host (or -h) [defaults to \'localhost\']');
  console.log('--port (or -p) [defaults to 8070]');
  console.log('or use a named option:')
  console.log('--named (or -n) [\'mitch\',\'patrick\']');
  console.log(namedWorkstations);
} else {
  console.log('Proxying: ', target);
  // Create your proxy server and set the target in the options.
  httpProxy.createProxyServer({ target: target }).listen(8070);
}
