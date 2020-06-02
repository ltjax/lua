#include <iostream>

#include <lua.hpp>


int main(int argc, char** argv)
{
  auto lua = lua_open();
  lua_close(lua);
  return 0;
}

