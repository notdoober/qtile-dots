return {
  "nvim-treesitter/nvim-treesitter",
  build = ":TSUpdate",
  config = function()
    vim.g.treesitter_config = {
      highlight = { enable = true },
      indent = { enable = true },
      ensure_installed = { "lua", "vim", "vimdoc", "bash", "json", "python" },
      auto_install = false,
    }
  end,
}
