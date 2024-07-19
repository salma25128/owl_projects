
odoo.define('pos_dev.TopButton',function(require){
    'use strict';

    const {Gui} = require('point_of_sale.Gui');
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

     class TopButton extends PosComponent{
      onClick(){
          Gui.showPopup("ErrorPopup",{
               title:this.env._t('Top Button Clicked'),
               body: this.env_t('Welcome to pos')
          });

      }
}
       TopButton.template='MenuButton';
        Registries.Component.add(TopButton);
});