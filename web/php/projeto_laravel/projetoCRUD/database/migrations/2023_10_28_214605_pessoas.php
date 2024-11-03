<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        schema::create('pessoas', function (Blueprint $table) {
            $table->increments('id');
            $table->string('nome', 50);
            $table->string('email');
            $table->string('telefone');
            $table->string('endereco');
            $table->date('data_nascimento');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        schema::drop('pessoas');
    }
};
