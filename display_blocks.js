(() => {
    const prototype = Blockly.blockRendering.PathObject.prototype;

    // Conserve le comportement original pour pouvoir le restaurer.
    window.__originalBlocklyDisabledRenderer ??= prototype.updateDisabled_;

    // Un bloc désactivé conserve désormais son apparence normale.
    prototype.updateDisabled_ = function () {
      this.setClass_("blocklyDisabled", false);
    };

    // Recalcule immédiatement les couleurs de tous les blocs affichés.
    for (const workspace of Blockly.Workspace.getAll()) {
      for (const block of workspace.getAllBlocks(false)) {
        if (block.rendered && typeof block.applyColour === "function") {
          block.applyColour();
        }
      }
    }
  })();