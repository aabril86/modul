# -*- coding: utf-8 -*-

from odoo import models, fields, api


class videoclub(models.Model):
    _name = 'videoclub.videoclub'
    _description = 'videoclub.videoclub'

    nom = fields.Char()
    direccio = fields.Char()
    propietari = fields.Char()
    obert = fields.Boolean()
    logo = fields.Image()
    phone = fields.Char(size=9)
    obertura = fields.Date()
    socis = fields.Integer()
    anotacions = fields.Text()
    pelicules = fields.One2many('videoclub.pelicula','videoclub', string="Pel·lícules")



    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100


class pelicula(models.Model):
    _name = 'videoclub.pelicula'
    _description = 'videoclub.pelicula'

    nombre = fields.Char()
    director = fields.Char()
    data = fields.Date()
    genere = fields.Text()
    videoclub = fields.Many2one('videoclub.videoclub','pelicules')   
