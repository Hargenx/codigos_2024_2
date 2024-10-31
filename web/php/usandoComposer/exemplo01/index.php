<?php

require 'vendor/autoload.php'; // Inclui o autoload do Composer

use Monolog\Logger;
use Monolog\Handler\StreamHandler;
use Monolog\Level; // Importe a classe Level

// Cria um logger
$log = new Logger('meu-log');
// Adiciona um handler que escreve para um arquivo com nível de WARNING
$log->pushHandler(new StreamHandler('meu-log.log', Level::Warning)); 

// Registra mensagens
$log->error('Isso é um erro');
$log->warning('Isso é um aviso');
$log->info('Isso é uma informação');
